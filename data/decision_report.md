# Decision Report

- generated_at: 2026-05-01T12:42:00.700091+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2797**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2797, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.77% | **+2.63%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.80% | **+2.10%** |
| MARKET_LONG | 20/20 | 100.0% | +1.67% | **+1.67%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.23% | **+1.34%** |
| ASK_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T12:41:58.791638+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.72% price=77985.9
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +66.84% | $13,648,803.99 |
| UB/USDT:USDT | +56.90% | $19,677,366.09 |
| BR/USDT:USDT | +37.71% | $25,476,759.96 |
| NFP/USDT:USDT | +35.88% | $1,307,441.39 |
| ORCA/USDT:USDT | +34.45% | $11,226,562.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NFP/USDT:USDT | below_relative_strength | +5.36% | +4.65% |
| ST/USDT:USDT | below_1h_threshold | +4.29% | +3.57% |
| ORCA/USDT:USDT | below_1h_threshold | +3.00% | +2.28% |
| TAO/USDT:USDT | below_1h_threshold | +1.39% | +0.67% |
| INJ/USDT:USDT | below_1h_threshold | +1.35% | +0.63% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
