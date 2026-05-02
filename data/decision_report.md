# Decision Report

- generated_at: 2026-05-02T00:51:49.527609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2848**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2848, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.73% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.89% | **+1.23%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.77% | **+0.97%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.16% | **+0.76%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.16% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T00:51:47.942455+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=78343.8
- Funnel: target 755 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +85.03% | $22,511,684.43 |
| FIGHT/USDT:USDT | +14.21% | $1,285,360.28 |
| CHILLGUY/USDT:USDT | +13.09% | $1,157,467.50 |
| BLESS/USDT:USDT | +10.75% | $1,300,661.76 |
| B/USDT:USDT | +9.14% | $64,921,865.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_relative_strength | +5.12% | +4.93% |
| CHIP/USDT:USDT | below_1h_threshold | +4.33% | +4.14% |
| KAT/USDT:USDT | below_1h_threshold | +4.08% | +3.88% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.65% | +3.45% |
| FIGHT/USDT:USDT | below_1h_threshold | +3.61% | +3.42% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
