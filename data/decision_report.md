# Decision Report

- generated_at: 2026-05-04T03:52:17.248859+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3139**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3139, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.72% | **+0.60%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_BB3S | 5/15 | 33.3% | +1.11% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.44% | **+1.83%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.41% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| MARKET_LONG | 20/20 | 100.0% | +0.57% | **+0.57%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.89% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T03:52:15.104535+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80157.3
- Funnel: target 757 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +48.49% | $235,143,096.59 |
| SKYAI/USDT:USDT | +43.43% | $37,926,163.16 |
| TAG/USDT:USDT | +42.44% | $6,360,325.15 |
| BSB/USDT:USDT | +41.66% | $16,244,943.42 |
| GIGA/USDT:USDT | +26.95% | $1,127,273.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.86% | +4.82% |
| DASH/USDT:USDT | below_1h_threshold | +4.48% | +4.44% |
| AIOT/USDT:USDT | below_1h_threshold | +2.72% | +2.69% |
| PARTI/USDT:USDT | below_1h_threshold | +2.25% | +2.22% |
| SIREN/USDT:USDT | below_1h_threshold | +1.52% | +1.49% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
