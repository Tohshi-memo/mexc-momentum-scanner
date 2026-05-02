# Decision Report

- generated_at: 2026-05-02T21:37:21.755580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2987**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2987, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/16 | 31.2% | +2.89% | **+0.90%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.74% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.10% | **+1.26%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.13% | **+1.17%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.75% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$102.70** / 初期 $100.00 (+2.70%)
- 確定トレード: 9件 (TP 4 / SL 4 / EXP 1)
- 最新: RAVE/USDT:USDT EXPIRED PnL +5.55% 残高後 $102.70
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T21:37:19.247765+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=78543.0
- Funnel: target 755 → liquid 166 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.2 >= 65=1, 4h RSI 70.8 >= 65=1, 4h RSI 84.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +43.15% | $304,009,266.83 |
| XNY/USDT:USDT | +16.98% | $2,047,861.99 |
| FHE/USDT:USDT | +15.96% | $1,000,003.18 |
| CHILLGUY/USDT:USDT | +13.43% | $1,166,321.30 |
| NAORIS/USDT:USDT | +10.96% | $4,418,087.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_relative_strength | +5.00% | +4.84% |
| SPACE/USDT:USDT | below_1h_threshold | +3.65% | +3.48% |
| CHILLGUY/USDT:USDT | below_1h_threshold | +3.30% | +3.13% |
| TRB/USDT:USDT | below_1h_threshold | +2.81% | +2.65% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.77% | +2.61% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
