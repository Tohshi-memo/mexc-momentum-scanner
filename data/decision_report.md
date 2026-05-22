# Decision Report

- generated_at: 2026-05-22T20:48:49.869967+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4740**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4740, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.46% | **+0.55%** |
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.53% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.74% | **+0.87%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.84% | **+0.71%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.43** / 初期 $100.00 (+24.43%)
- 確定: 586件 (Win 149 / Loss 189 / Flat 248) / skip 715件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $124.43

## 4. Latest Market Context

- 更新: 2026-05-22T20:48:47.800529+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=75913.9
- Funnel: target 764 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +77.05% | $38,752,959.10 |
| BILL/USDT:USDT | +20.18% | $16,040,232.09 |
| BEAT/USDT:USDT | +6.83% | $38,642,025.22 |
| LAB/USDT:USDT | +3.29% | $29,050,130.70 |
| GUA/USDT:USDT | +2.94% | $1,170,098.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.81% | +3.70% |
| GUA/USDT:USDT | below_1h_threshold | +2.64% | +2.52% |
| INJ/USDT:USDT | below_1h_threshold | +1.95% | +1.83% |
| SAGA/USDT:USDT | below_1h_threshold | +1.81% | +1.69% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.79% | +1.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
