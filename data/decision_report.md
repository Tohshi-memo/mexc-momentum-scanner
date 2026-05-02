# Decision Report

- generated_at: 2026-05-02T21:12:10.174963+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2983**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2983, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/15 | 33.3% | +1.45% | **+0.48%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.28% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.50% | **+0.50%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.35% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T21:12:08.167604+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78452.0
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XNY/USDT:USDT | +14.37% | $1,957,541.03 |
| NAORIS/USDT:USDT | +13.86% | $4,056,170.96 |
| BSB/USDT:USDT | +12.35% | $11,481,121.37 |
| LUNC/USDT:USDT | +11.79% | $27,980,577.45 |
| CHILLGUY/USDT:USDT | +10.29% | $1,123,978.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XNY/USDT:USDT | below_1h_threshold | +3.30% | +3.25% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.37% | +2.32% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.09% | +2.05% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.64% | +1.60% |
| ACH/USDT:USDT | below_1h_threshold | +1.40% | +1.35% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
