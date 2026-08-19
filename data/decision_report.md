# Decision Report

- generated_at: 2026-08-19T08:06:33.778799+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11964**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11964, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.14% | **-0.11%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.43% | **-0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.03% | **+1.62%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.63% | **+1.58%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.37% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.17% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$635.52** / 初期 $100.00 (+535.52%)
- 確定: 4225件 (Win 1301 / Loss 1377 / Flat 1547) / skip 4300件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKHYSTOCK/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $635.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3554件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0623 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.62** / 初期 $100.00 (+18.62%)
- 確定: 1741件 (Win 520 / Loss 661 / Flat 560) / pending 2件 / skip 1691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KORU/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $118.62

## 6. Latest Market Context

- 更新: 2026-08-19T08:06:18.222573+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64280.6
- Funnel: target 992 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +70.72% | $64,467,635.53 |
| HEMI/USDT:USDT | +29.25% | $2,375,003.87 |
| UNITREE/USDT:USDT | +24.63% | $14,903,736.34 |
| NIULAI/USDT:USDT | +12.01% | $5,205,081.47 |
| SKUU/USDT:USDT | +11.00% | $2,691,742.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +4.27% | +4.24% |
| MUU/USDT:USDT | below_1h_threshold | +3.63% | +3.60% |
| KORU/USDT:USDT | below_1h_threshold | +3.55% | +3.52% |
| SKUU/USDT:USDT | below_1h_threshold | +3.35% | +3.33% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.32% | +3.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
