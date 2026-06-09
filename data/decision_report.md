# Decision Report

- generated_at: 2026-06-09T12:32:58.287201+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6135**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=6135, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.68% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.84% | **+0.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.75% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.60% | **+0.39%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.65% | **+0.36%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.35% | **+0.23%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.17% | **+0.13%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.90** / 初期 $100.00 (+51.90%)
- 確定: 1175件 (Win 295 / Loss 366 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POWER/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $151.90

## 4. Latest Market Context

- 更新: 2026-06-09T12:32:55.729072+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=62616.9
- Funnel: target 774 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +55.39% | $22,052,551.67 |
| SLX/USDT:USDT | +27.29% | $5,441,571.07 |
| POWER/USDT:USDT | +23.43% | $2,934,128.90 |
| PLAY/USDT:USDT | +17.05% | $2,082,368.00 |
| WLD/USDT:USDT | +11.49% | $132,352,997.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +4.70% | +4.80% |
| CHIP/USDT:USDT | below_1h_threshold | +2.85% | +2.95% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.83% | +2.93% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.46% | +2.56% |
| JTO/USDT:USDT | below_1h_threshold | +2.03% | +2.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
