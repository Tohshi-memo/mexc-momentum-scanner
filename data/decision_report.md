# Decision Report

- generated_at: 2026-07-04T05:57:07.619395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8224**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8224, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.87%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.87% | **-1.87%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.50% | **+0.15%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.90% | **+1.90%** |
| ASK_LONG | 20/20 | 100.0% | +1.77% | **+1.77%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.90% | **+1.30%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.64% | **+1.07%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$309.68** / 初期 $100.00 (+209.68%)
- 確定: 2541件 (Win 791 / Loss 846 / Flat 904) / skip 2244件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NEX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $309.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 620件 (Win 149 / Loss 150 / Flat 321) / skip 1015件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0701 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NEX/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-07-04T05:57:00.009957+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=62431.3
- Funnel: target 834 → liquid 157 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1, 4h RSI 76.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +78.04% | $4,612,585.70 |
| TLM/USDT:USDT | +61.95% | $42,841,699.83 |
| HMSTR/USDT:USDT | +40.63% | $3,512,305.28 |
| BAS/USDT:USDT | +34.56% | $4,152,190.05 |
| MAGMA/USDT:USDT | +27.40% | $15,689,633.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +5.00% | +5.37% |
| VELVET/USDT:USDT | below_1h_threshold | +4.01% | +4.38% |
| M/USDT:USDT | below_1h_threshold | +3.70% | +4.07% |
| NIL/USDT:USDT | below_1h_threshold | +3.63% | +4.00% |
| HMSTR/USDT:USDT | below_1h_threshold | +3.58% | +3.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
