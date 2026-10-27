# Decision Report

- generated_at: 2026-10-27T01:21:28.322638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17545**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17545, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_BB3S | 9/19 | 47.4% | +1.72% | **+0.81%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.02% | **+0.92%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +6.68% | **+0.67%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.89% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7385件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$323.44** / 初期 $100.00 (+223.44%)
- 確定: 4074件 (Win 1121 / Loss 955 / Flat 1998) / skip 6882件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_8PCT` (selected_by_robust_growth_score) / robust_score +0.1194 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $323.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5704件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000345 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-27T01:21:13.397815+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80198.5
- Funnel: target 1078 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +233.90% | $26,159,638.34 |
| SYN/USDT:USDT | +16.79% | $1,487,113.61 |
| ARIA/USDT:USDT | +16.14% | $1,002,045.50 |
| DOOD/USDT:USDT | +15.28% | $4,375,260.83 |
| DNA/USDT:USDT | +14.48% | $1,249,238.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DNA/USDT:USDT | below_1h_threshold | +4.15% | +4.14% |
| SNXX/USDT:USDT | below_1h_threshold | +2.10% | +2.10% |
| KORU/USDT:USDT | below_1h_threshold | +1.68% | +1.67% |
| JCT/USDT:USDT | below_1h_threshold | +1.36% | +1.36% |
| BR/USDT:USDT | below_1h_threshold | +1.11% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
