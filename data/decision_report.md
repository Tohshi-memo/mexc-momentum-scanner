# Decision Report

- generated_at: 2026-09-05T17:06:31.814743+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13758**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13758, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.77% | **+0.35%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.06% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.44% | **+1.22%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.50% | **+1.13%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.91** / 初期 $100.00 (+759.91%)
- 確定: 5064件 (Win 1521 / Loss 1652 / Flat 1891) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $859.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.52** / 初期 $100.00 (+88.52%)
- 確定: 2503件 (Win 698 / Loss 590 / Flat 1215) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0338 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.53** / 初期 $100.00 (+19.53%)
- 確定: 2379件 (Win 706 / Loss 903 / Flat 770) / pending 5件 / skip 2847件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000245 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.53

## 6. Latest Market Context

- 更新: 2026-09-05T17:06:18.335398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=80003.1
- Funnel: target 1050 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +14.86% | $24,073,928.20 |
| USELESS/USDT:USDT | +12.93% | $19,789,952.79 |
| NIULAI/USDT:USDT | +11.77% | $2,156,567.87 |
| MAGMA/USDT:USDT | +9.54% | $2,108,822.68 |
| VELVET/USDT:USDT | +7.98% | $1,021,421.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +3.03% | +3.02% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.73% | +2.73% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +2.19% | +2.18% |
| USELESS/USDT:USDT | below_1h_threshold | +2.08% | +2.08% |
| PONS/USDT:USDT | below_1h_threshold | +1.75% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
