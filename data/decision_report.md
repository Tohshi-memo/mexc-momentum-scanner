# Decision Report

- generated_at: 2026-05-04T03:27:11.491694+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3135**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3135, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_BB3S | 5/17 | 29.4% | +0.50% | **+0.15%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.33% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.95% | **+2.21%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.11% | **+1.27%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.39% | **+1.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.24% | **+1.12%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T03:27:09.331916+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=80055.2
- Funnel: target 757 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +42.85% | $233,179,996.85 |
| TAG/USDT:USDT | +42.82% | $5,585,398.39 |
| BSB/USDT:USDT | +32.86% | $15,320,049.48 |
| GIGA/USDT:USDT | +29.15% | $1,119,878.69 |
| SKYAI/USDT:USDT | +28.16% | $36,475,436.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +1.43% | +1.52% |
| EDGE/USDT:USDT | below_1h_threshold | +1.24% | +1.33% |
| DASH/USDT:USDT | below_1h_threshold | +1.13% | +1.22% |
| MERL/USDT:USDT | below_1h_threshold | +1.09% | +1.18% |
| ZEN/USDT:USDT | below_1h_threshold | +0.91% | +1.00% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
