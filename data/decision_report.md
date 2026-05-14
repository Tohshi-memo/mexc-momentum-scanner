# Decision Report

- generated_at: 2026-05-14T01:58:04.421938+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4264**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.72% / filled 20/20。**
- 全期間 MARKET基準: n=4264, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.29% | **+1.16%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| MARKET | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.68% | **+0.41%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.33% | **+0.93%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.83% | **+0.66%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.84% | **+0.50%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.35% | **+0.32%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 482件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T01:57:58.801672+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79580.1
- Funnel: target 765 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +24.80% | $6,439,847.77 |
| TROLLSOL/USDT:USDT | +21.47% | $1,921,808.63 |
| CSCOSTOCK/USDT:USDT | +21.34% | $4,717,168.21 |
| UP/USDT:USDT | +20.98% | $4,944,549.72 |
| SAGA/USDT:USDT | +19.35% | $16,378,556.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.85% | +4.80% |
| GIGA/USDT:USDT | below_1h_threshold | +3.47% | +3.42% |
| TRUTH/USDT:USDT | below_1h_threshold | +3.08% | +3.03% |
| BILL/USDT:USDT | below_1h_threshold | +2.80% | +2.75% |
| VELVET/USDT:USDT | below_1h_threshold | +2.25% | +2.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
