# Decision Report

- generated_at: 2026-05-08T19:02:21.970817+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3817**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=3817, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/17 | 29.4% | +1.53% | **+0.45%** |
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.99% | **+0.44%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.94% | **+0.42%** |
| ASK_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.12% | **+0.06%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 186件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T19:02:19.744506+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=79996.4
- Funnel: target 768 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +12.28% | $2,165,609.45 |
| JUP/USDT:USDT | +10.15% | $5,752,766.67 |
| AKT/USDT:USDT | +10.06% | $1,217,417.06 |
| CHIP/USDT:USDT | +8.14% | $51,398,161.63 |
| JTO/USDT:USDT | +7.99% | $10,496,031.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +1.26% | +1.32% |
| RKLBSTOCK/USDT:USDT | below_1h_threshold | +0.56% | +0.62% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.55% | +0.61% |
| JTO/USDT:USDT | below_1h_threshold | +0.52% | +0.58% |
| CHIP/USDT:USDT | below_1h_threshold | +0.48% | +0.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
