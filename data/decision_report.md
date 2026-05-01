# Decision Report

- generated_at: 2026-05-01T19:32:09.958186+00:00
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

- 更新: 2026-05-01T19:32:05.772889+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=78327.3
- Funnel: target 756 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +16.32% | $2,500,499.31 |
| ZEN/USDT:USDT | +11.04% | $5,660,499.36 |
| LAB/USDT:USDT | +9.99% | $1,263,201.87 |
| ZEC/USDT:USDT | +7.18% | $300,864,078.29 |
| SQD/USDT:USDT | +5.90% | $2,077,022.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEN/USDT:USDT | below_1h_threshold | +2.16% | +2.24% |
| PHAROS/USDT:USDT | below_1h_threshold | +2.02% | +2.10% |
| TRB/USDT:USDT | below_1h_threshold | +1.74% | +1.83% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.49% | +1.57% |
| BLEND/USDT:USDT | below_1h_threshold | +1.42% | +1.50% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
