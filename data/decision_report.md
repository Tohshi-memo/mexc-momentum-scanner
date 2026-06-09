# Decision Report

- generated_at: 2026-06-09T13:02:25.990110+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6136**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=6136, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.84% | **+0.43%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.48% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.27% | **+0.19%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.26% | **+0.16%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.86% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.14** / 初期 $100.00 (+51.14%)
- 確定: 1176件 (Win 295 / Loss 367 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $151.14

## 4. Latest Market Context

- 更新: 2026-06-09T13:02:23.373655+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62603.2
- Funnel: target 774 → liquid 144 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +53.66% | $22,485,373.50 |
| SLX/USDT:USDT | +27.57% | $5,464,707.33 |
| POWER/USDT:USDT | +21.85% | $3,164,382.94 |
| PLAY/USDT:USDT | +18.33% | $2,187,718.19 |
| CHIP/USDT:USDT | +12.98% | $2,097,612.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +1.31% | +1.32% |
| HOME/USDT:USDT | below_1h_threshold | +1.18% | +1.20% |
| ZEST/USDT:USDT | below_1h_threshold | +0.51% | +0.52% |
| JTO/USDT:USDT | below_1h_threshold | +0.36% | +0.37% |
| ALLO/USDT:USDT | below_1h_threshold | +0.34% | +0.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
