# Decision Report

- generated_at: 2026-07-07T14:55:43.153610+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8438**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8438, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.35% | **+0.40%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.02% | **+1.72%** |
| ASK_LONG | 20/20 | 100.0% | +1.63% | **+1.63%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.50% | **+0.98%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.20% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$100.55** / 初期 $100.00 (+0.55%)
- 確定トレード: 69件 (TP 23 / SL 45 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.55
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$320.89** / 初期 $100.00 (+220.89%)
- 確定: 2645件 (Win 843 / Loss 896 / Flat 906) / skip 2354件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $320.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 640件 (Win 152 / Loss 158 / Flat 330) / skip 1209件
- 成長率目線: 平均log +0.000083 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0249 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-07T14:55:37.564691+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.53% price=63355.2
- Funnel: target 847 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1, 4h RSI 91.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +112.73% | $15,483,537.98 |
| TAC/USDT:USDT | +65.91% | $16,612,743.79 |
| BLUR/USDT:USDT | +42.54% | $13,126,963.60 |
| M/USDT:USDT | +22.78% | $1,092,861.80 |
| EDGE/USDT:USDT | +21.19% | $6,822,999.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.86% | +3.33% |
| LDO/USDT:USDT | below_1h_threshold | +2.57% | +2.05% |
| RIF/USDT:USDT | below_1h_threshold | +2.24% | +1.72% |
| ZEC/USDT:USDT | below_1h_threshold | +2.06% | +1.54% |
| ALLO/USDT:USDT | below_1h_threshold | +1.83% | +1.30% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
