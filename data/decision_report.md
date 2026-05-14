# Decision Report

- generated_at: 2026-05-14T01:28:00.142650+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4263**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4263, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +0.68% | **+0.61%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.14% | **+0.14%** |
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.81% | **+0.98%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.15% | **+0.86%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.92% | **+0.51%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.56% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 41件 (TP 10 / SL 28 / EXP 3)
- 最新: SAGA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 343件 (Win 94 / Loss 125 / Flat 124) / skip 481件
- 成長率目線: 平均log +0.000512 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T01:27:56.646833+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79583.5
- Funnel: target 761 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +26.44% | $6,237,764.34 |
| TROLLSOL/USDT:USDT | +22.94% | $1,891,692.10 |
| CSCOSTOCK/USDT:USDT | +21.46% | $4,673,830.90 |
| UP/USDT:USDT | +20.86% | $4,931,939.46 |
| BB/USDT:USDT | +16.71% | $2,264,103.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +3.12% | +3.06% |
| USELESS/USDT:USDT | below_1h_threshold | +2.54% | +2.48% |
| EDU/USDT:USDT | below_1h_threshold | +2.51% | +2.45% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.42% | +2.37% |
| BILL/USDT:USDT | below_1h_threshold | +2.08% | +2.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
