# Decision Report

- generated_at: 2026-05-31T06:08:12.501245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5174**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.37% / filled 20/20。**
- 全期間 MARKET基準: n=5174, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.96% | **+0.29%** |
| ASK | 20/20 | 100.0% | +0.27% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.72% | **+0.72%** |
| ASK_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.69% | **+0.54%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.76% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$97.61** / 初期 $100.00 (-2.39%)
- 確定トレード: 79件 (TP 23 / SL 53 / EXP 3)
- 最新: ID/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.91** / 初期 $100.00 (+22.91%)
- 確定: 809件 (Win 184 / Loss 243 / Flat 382) / skip 926件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +6.32%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $122.91

## 4. Latest Market Context

- 更新: 2026-05-31T06:08:09.447865+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=73960.1
- Funnel: target 773 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +22.85% | $1,313,959.56 |
| TA/USDT:USDT | +22.79% | $2,372,655.90 |
| PORTAL/USDT:USDT | +18.82% | $10,879,335.49 |
| MYX/USDT:USDT | +12.49% | $2,460,781.00 |
| LAB/USDT:USDT | +10.51% | $179,500,885.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +1.59% | +1.69% |
| H/USDT:USDT | below_1h_threshold | +1.58% | +1.67% |
| STG/USDT:USDT | below_1h_threshold | +1.54% | +1.64% |
| TA/USDT:USDT | below_1h_threshold | +1.46% | +1.55% |
| BILL/USDT:USDT | below_1h_threshold | +0.60% | +0.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
