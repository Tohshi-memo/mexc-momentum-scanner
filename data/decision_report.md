# Decision Report

- generated_at: 2026-11-22T14:16:23.515447+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19390**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19390, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_BB3S | 4/17 | 23.5% | +1.46% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.84% | **+2.84%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.47% | **+1.36%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,809.82** / 初期 $100.00 (+1709.82%)
- 確定: 7500件 (Win 2155 / Loss 2415 / Flat 2930) / skip 8451件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $1,809.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$458.76** / 初期 $100.00 (+358.76%)
- 確定: 5154件 (Win 1374 / Loss 1111 / Flat 2669) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0703 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $458.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7550件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000378 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T14:16:07.692044+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=60739.1
- Funnel: target 1086 → liquid 103 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +45.08% | $34,788,467.78 |
| CLAUDIA/USDT:USDT | +40.73% | $2,717,108.01 |
| DGAI/USDT:USDT | +26.64% | $1,139,851.97 |
| NIGHT/USDT:USDT | +13.83% | $1,963,356.56 |
| DCTY/USDT:USDT | +12.68% | $1,823,295.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.61% | +4.57% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +3.79% | +3.75% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.70% | +1.66% |
| VVV/USDT:USDT | below_1h_threshold | +1.04% | +1.00% |
| ZRO/USDT:USDT | below_1h_threshold | +0.92% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
