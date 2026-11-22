# Decision Report

- generated_at: 2026-11-22T14:26:10.582101+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19392**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19392, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.84% | **+2.84%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.16% | **+1.73%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 284件 (TP 103 / SL 173 / EXP 8)
- 最新: MMT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,818.78** / 初期 $100.00 (+1718.78%)
- 確定: 7502件 (Win 2156 / Loss 2416 / Flat 2930) / skip 8451件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,818.78

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.30** / 初期 $100.00 (+360.30%)
- 確定: 5156件 (Win 1375 / Loss 1112 / Flat 2669) / skip 7647件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0592 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $460.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7552件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000377 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-22T14:25:58.483356+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=60664.1
- Funnel: target 1086 → liquid 104 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +41.70% | $35,760,026.09 |
| CLAUDIA/USDT:USDT | +39.15% | $2,723,720.72 |
| DGAI/USDT:USDT | +26.07% | $1,157,706.52 |
| NIGHT/USDT:USDT | +13.69% | $2,010,534.10 |
| VELVET/USDT:USDT | +13.62% | $1,328,952.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.60% | +2.68% |
| BLESS/USDT:USDT | below_1h_threshold | +2.27% | +2.35% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.11% | +2.19% |
| VVV/USDT:USDT | below_1h_threshold | +1.18% | +1.26% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.61% | +0.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
