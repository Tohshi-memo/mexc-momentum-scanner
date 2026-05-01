# Decision Report

- generated_at: 2026-05-01T10:37:03.698143+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2784**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2784, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.28% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +4.93% | **+3.70%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.45% | **+2.07%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.90% | **+1.74%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.39% | **+1.56%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T10:37:01.602741+00:00 / 保存件数 268/288
- BTC: STAGNANT 1h +0.05% price=77277.5
- Funnel: target 760 → liquid 199 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 78.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +62.23% | $9,886,987.50 |
| UB/USDT:USDT | +47.15% | $13,161,748.52 |
| ZEREBRO/USDT:USDT | +46.11% | $8,326,265.78 |
| BR/USDT:USDT | +36.31% | $23,721,931.73 |
| ORCA/USDT:USDT | +30.41% | $10,622,931.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +4.62% | +4.57% |
| DRIFT/USDT:USDT | below_1h_threshold | +3.74% | +3.69% |
| SIREN/USDT:USDT | below_1h_threshold | +2.59% | +2.54% |
| LAB/USDT:USDT | below_1h_threshold | +2.52% | +2.47% |
| BRETT/USDT:USDT | below_1h_threshold | +1.71% | +1.66% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
