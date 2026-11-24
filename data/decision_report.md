# Decision Report

- generated_at: 2026-11-24T21:16:34.471699+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19577**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19577, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.31% | **-0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.30% | **+0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.36% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.18% | **+1.42%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.21% | **+1.33%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 286件 (TP 104 / SL 174 / EXP 8)
- 最新: NVD/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,989.52** / 初期 $100.00 (+1889.52%)
- 確定: 7609件 (Win 2191 / Loss 2449 / Flat 2969) / skip 8529件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,989.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7768件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0023 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7742件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000058 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-24T21:16:17.845468+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=59743.5
- Funnel: target 1092 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GUA/USDT:USDT | +44.56% | $1,160,635.51 |
| KIMCHI/USDT:USDT | +11.22% | $1,665,425.52 |
| BTW/USDT:USDT | +6.95% | $3,162,764.30 |
| IRYS/USDT:USDT | +5.84% | $1,546,532.53 |
| SNXX/USDT:USDT | +5.35% | $41,585,916.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVDL/USDT:USDT | below_1h_threshold | +3.74% | +3.77% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +2.66% | +2.70% |
| SNXX/USDT:USDT | below_1h_threshold | +2.63% | +2.66% |
| NVIDIA/USDT:USDT | below_1h_threshold | +1.60% | +1.64% |
| AKE/USDT:USDT | below_1h_threshold | +1.42% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
