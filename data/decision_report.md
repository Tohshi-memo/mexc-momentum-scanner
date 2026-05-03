# Decision Report

- generated_at: 2026-05-03T01:32:20.488453+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3009**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.91% / filled 20/20。**
- 全期間 MARKET基準: n=3009, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_BB3S | 8/18 | 44.4% | +0.82% | **+0.36%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.01% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.41% | **+6.41%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.56% | **+0.86%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.59% | **+0.63%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.38% | **+0.62%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.11% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T01:32:18.513032+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=78212.6
- Funnel: target 755 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPACE/USDT:USDT | +21.65% | $1,823,874.58 |
| LUNC/USDT:USDT | +20.12% | $34,189,202.94 |
| BABY/USDT:USDT | +16.54% | $1,779,148.91 |
| FHE/USDT:USDT | +16.01% | $2,239,242.18 |
| BIANRENSHENG/USDT:USDT | +14.52% | $1,890,822.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USTC/USDT:USDT | below_1h_threshold | +4.61% | +4.98% |
| ORCA/USDT:USDT | below_1h_threshold | +2.32% | +2.69% |
| LUNANEW/USDT:USDT | below_1h_threshold | +1.43% | +1.80% |
| TAC/USDT:USDT | below_1h_threshold | +1.36% | +1.72% |
| LUNC/USDT:USDT | below_1h_threshold | +1.25% | +1.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
