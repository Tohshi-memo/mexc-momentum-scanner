# Decision Report

- generated_at: 2026-08-02T01:46:25.641096+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10132**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10132, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.37% | **-1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.43% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.04% | **+2.13%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.81% | **+2.11%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.46% | **+1.48%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$580.23** / 初期 $100.00 (+480.23%)
- 確定: 3651件 (Win 1162 / Loss 1193 / Flat 1296) / skip 3042件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $580.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1280件 (Win 359 / Loss 297 / Flat 624) / skip 2263件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1326 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.04** / 初期 $100.00 (+13.04%)
- 確定: 940件 (Win 300 / Loss 365 / Flat 275) / pending 2件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000469 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $113.04

## 6. Latest Market Context

- 更新: 2026-08-02T01:46:13.431939+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=62983.0
- Funnel: target 922 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +41.14% | $23,611,320.35 |
| UAI/USDT:USDT | +22.52% | $18,649,912.92 |
| BLESS/USDT:USDT | +14.90% | $5,743,108.56 |
| KOMA/USDT:USDT | +14.12% | $13,509,440.27 |
| ON/USDT:USDT | +11.25% | $6,314,651.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EUL/USDT:USDT | below_1h_threshold | +4.39% | +4.11% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +4.26% | +3.98% |
| TSEMSTOCK/USDT:USDT | below_1h_threshold | +2.79% | +2.51% |
| SYN/USDT:USDT | below_1h_threshold | +2.51% | +2.23% |
| WLD/USDT:USDT | below_1h_threshold | +2.42% | +2.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
