# Decision Report

- generated_at: 2026-07-03T06:53:43.673607+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8138**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8138, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_BB3S | 2/19 | 10.5% | +2.75% | **+0.29%** |
| LIMIT_6PCT | 6/20 | 30.0% | -0.08% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.41% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.27% | **+0.79%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$288.33** / 初期 $100.00 (+188.33%)
- 確定: 2459件 (Win 758 / Loss 820 / Flat 881) / skip 2240件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $288.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 592件 (Win 143 / Loss 139 / Flat 310) / skip 957件
- 成長率目線: 平均log +0.000113 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0096 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.89

## 5. Latest Market Context

- 更新: 2026-07-03T06:53:37.997770+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=61673.7
- Funnel: target 834 → liquid 166 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.8 >= 65=1, 4h RSI 66.6 >= 65=1, 4h RSI 94.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +42.23% | $1,137,224.73 |
| ZKP/USDT:USDT | +30.41% | $3,148,847.67 |
| RIF/USDT:USDT | +25.56% | $7,255,267.27 |
| NOM/USDT:USDT | +22.45% | $2,830,786.98 |
| MAGMA/USDT:USDT | +20.49% | $6,483,153.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.24% | +4.24% |
| SYN/USDT:USDT | below_1h_threshold | +3.95% | +3.95% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.52% | +2.52% |
| ZKP/USDT:USDT | below_1h_threshold | +2.11% | +2.11% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.00% | +2.00% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
