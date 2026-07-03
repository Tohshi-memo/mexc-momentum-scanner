# Decision Report

- generated_at: 2026-07-03T05:48:11.715338+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8136**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8136, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.78% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.21% | **+0.99%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.37% | **+0.95%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.82% | **+0.82%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +6.84% | **+0.68%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.13% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$286.14** / 初期 $100.00 (+186.14%)
- 確定: 2457件 (Win 757 / Loss 820 / Flat 880) / skip 2240件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $286.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.89** / 初期 $100.00 (+6.89%)
- 確定: 590件 (Win 143 / Loss 139 / Flat 308) / skip 957件
- 成長率目線: 平均log +0.000113 / 幾何平均 +0.011% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0096 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +0.69% 残高後 $106.89

## 5. Latest Market Context

- 更新: 2026-07-03T05:48:01.715701+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=61635.7
- Funnel: target 834 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.2 >= 65=1, 4h RSI 69.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +40.48% | $6,518,194.80 |
| ZKP/USDT:USDT | +28.80% | $2,724,065.35 |
| MAGMA/USDT:USDT | +28.24% | $6,183,454.51 |
| NOM/USDT:USDT | +20.78% | $2,372,866.43 |
| GUA/USDT:USDT | +20.56% | $10,156,081.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +2.66% | +2.31% |
| SPX/USDT:USDT | below_1h_threshold | +2.58% | +2.23% |
| LIT/USDT:USDT | below_1h_threshold | +2.07% | +1.72% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.06% | +1.71% |
| RPL/USDT:USDT | below_1h_threshold | +1.93% | +1.58% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
