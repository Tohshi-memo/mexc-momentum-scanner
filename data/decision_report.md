# Decision Report

- generated_at: 2026-08-14T18:16:41.439587+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11592**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11592, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 19/20 | 95.0% | +1.38% | **+1.31%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.86% | **+0.82%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.24% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.02% | **+1.82%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.37% | **+1.68%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$646.40** / 初期 $100.00 (+546.40%)
- 確定: 4060件 (Win 1275 / Loss 1334 / Flat 1451) / skip 4093件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $646.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.36** / 初期 $100.00 (+52.36%)
- 確定: 1659件 (Win 476 / Loss 400 / Flat 783) / skip 3344件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0971 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $152.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.82** / 初期 $100.00 (+16.82%)
- 確定: 1543件 (Win 468 / Loss 591 / Flat 484) / pending 6件 / skip 1518件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.82

## 6. Latest Market Context

- 更新: 2026-08-14T18:16:26.548565+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=62991.9
- Funnel: target 985 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +32.08% | $73,504,844.17 |
| US/USDT:USDT | +24.95% | $6,322,597.73 |
| ACE/USDT:USDT | +10.86% | $55,395,530.09 |
| ACU/USDT:USDT | +5.99% | $2,500,515.05 |
| BANK/USDT:USDT | +4.50% | $2,300,509.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +2.94% | +2.94% |
| BTW/USDT:USDT | below_1h_threshold | +2.26% | +2.26% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.74% | +1.74% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.63% |
| BR/USDT:USDT | below_1h_threshold | +1.25% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
