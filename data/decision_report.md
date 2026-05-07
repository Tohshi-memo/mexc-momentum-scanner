# Decision Report

- generated_at: 2026-05-07T21:22:35.794859+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3700**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=3700, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/17 | 17.6% | +4.70% | **+0.83%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.51% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.49% | **+2.49%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.22% | **+0.18%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.08% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 72件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T21:22:32.395291+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=79820.1
- Funnel: target 765 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +52.40% | $6,572,060.56 |
| TST/USDT:USDT | +32.71% | $5,410,428.75 |
| NIL/USDT:USDT | +26.20% | $12,781,607.84 |
| IRENSTOCK/USDT:USDT | +14.33% | $4,418,097.13 |
| NOT/USDT:USDT | +14.25% | $10,074,484.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| D/USDT:USDT | below_1h_threshold | +2.42% | +2.44% |
| HIGH/USDT:USDT | below_1h_threshold | +2.05% | +2.07% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.81% | +1.83% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.93% | +0.95% |
| LINEA/USDT:USDT | below_1h_threshold | +0.91% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
