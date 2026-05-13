# Decision Report

- generated_at: 2026-05-13T01:17:57.814321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4177**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=4177, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.17% | **+1.11%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.74% | **+0.96%** |
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.75% | **+0.67%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.35% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定: 313件 (Win 91 / Loss 111 / Flat 111) / skip 425件
- 成長率目線: 平均log +0.000597 / 幾何平均 +0.060% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DYM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $120.56

## 4. Latest Market Context

- 更新: 2026-05-13T01:17:54.515921+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=80831.3
- Funnel: target 759 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +15.57% | $1,071,822.97 |
| IRYS/USDT:USDT | +14.95% | $2,187,074.68 |
| AKT/USDT:USDT | +14.58% | $2,718,454.16 |
| PEAQ/USDT:USDT | +14.22% | $2,153,588.11 |
| LAB/USDT:USDT | +8.99% | $105,772,421.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEAQ/USDT:USDT | below_1h_threshold | +3.14% | +2.94% |
| IRYS/USDT:USDT | below_1h_threshold | +2.48% | +2.28% |
| BRETT/USDT:USDT | below_1h_threshold | +2.24% | +2.04% |
| AKT/USDT:USDT | below_1h_threshold | +1.98% | +1.79% |
| NEAR/USDT:USDT | below_1h_threshold | +1.91% | +1.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
