# Decision Report

- generated_at: 2026-05-01T19:26:41.052226+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2824**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.08% / filled 20/20。**
- 全期間 MARKET基準: n=2824, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.32% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 2/15 | 13.3% | +3.33% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.44% | **+0.18%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.38% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$103.54** / 初期 $100.00 (+3.54%)
- 確定トレード: 5件 (TP 4 / SL 1 / EXP 0)
- 最新: NAORIS/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.54
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T19:26:37.587558+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78410.8
- Funnel: target 756 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +19.10% | $2,406,163.50 |
| ZEN/USDT:USDT | +10.91% | $5,520,757.33 |
| LAB/USDT:USDT | +7.95% | $1,209,044.04 |
| ZEC/USDT:USDT | +7.03% | $299,664,895.01 |
| SQD/USDT:USDT | +5.67% | $2,073,410.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +3.50% | +3.48% |
| ZEN/USDT:USDT | below_1h_threshold | +1.99% | +1.96% |
| PHAROS/USDT:USDT | below_1h_threshold | +1.55% | +1.52% |
| TRB/USDT:USDT | below_1h_threshold | +1.53% | +1.50% |
| BSB/USDT:USDT | below_1h_threshold | +1.40% | +1.37% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
