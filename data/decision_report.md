# Decision Report

- generated_at: 2026-05-01T10:50:00.652376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2788**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2788, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.69% | **-1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.44% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +6.26% | **+3.13%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +3.07% | **+3.07%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.42% | **+1.88%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.40% | **+1.87%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.66% | **+1.73%** |

## 2. $100 Live Portfolio

- 残高: **$101.50** / 初期 $100.00 (+1.50%)
- 確定トレード: 3件 (TP 2 / SL 1 / EXP 0)
- 最新: GRIFFAIN/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.50
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T10:49:55.952231+00:00 / 保存件数 271/288
- BTC: STAGNANT 1h -0.00% price=77236.0
- Funnel: target 760 → liquid 200 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1, 4h RSI 83.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UB/USDT:USDT | +75.61% | $14,692,517.13 |
| B/USDT:USDT | +63.59% | $10,168,709.93 |
| ZEREBRO/USDT:USDT | +48.97% | $8,546,681.84 |
| BR/USDT:USDT | +41.85% | $24,040,690.65 |
| ORCA/USDT:USDT | +29.26% | $10,661,728.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DRIFT/USDT:USDT | below_1h_threshold | +4.79% | +4.80% |
| LAB/USDT:USDT | below_1h_threshold | +3.24% | +3.24% |
| TAC/USDT:USDT | below_1h_threshold | +2.58% | +2.58% |
| BRETT/USDT:USDT | below_1h_threshold | +2.17% | +2.17% |
| SIREN/USDT:USDT | below_1h_threshold | +2.06% | +2.06% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
