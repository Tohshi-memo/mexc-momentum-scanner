# Decision Report

- generated_at: 2026-05-02T20:42:16.561193+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2981**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2981, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/15 | 33.3% | +1.45% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.71% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.11% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +5.69% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.55% | **+0.76%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.95% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T20:42:14.591723+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78433.5
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XNY/USDT:USDT | +15.16% | $1,864,683.10 |
| LUNC/USDT:USDT | +10.70% | $27,528,028.40 |
| CHILLGUY/USDT:USDT | +10.36% | $1,142,381.86 |
| BEAT/USDT:USDT | +7.80% | $3,211,123.43 |
| ZKSYNC/USDT:USDT | +7.65% | $1,297,485.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACH/USDT:USDT | below_1h_threshold | +3.83% | +3.84% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +3.73% | +3.74% |
| BEAT/USDT:USDT | below_1h_threshold | +3.31% | +3.32% |
| BSB/USDT:USDT | below_1h_threshold | +3.00% | +3.01% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.61% | +2.63% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
