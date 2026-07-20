# Decision Report

- generated_at: 2026-07-20T09:21:08.754369+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9103**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9103, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.76%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.35% | **+0.09%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.12% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +7.03% | **+4.22%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.96% | **+2.37%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.68% | **+0.80%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$404.39** / 初期 $100.00 (+304.39%)
- 確定: 3165件 (Win 989 / Loss 1003 / Flat 1173) / skip 2499件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $404.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.73** / 初期 $100.00 (+26.73%)
- 確定: 1064件 (Win 276 / Loss 218 / Flat 570) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0605 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $126.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定: 302件 (Win 100 / Loss 133 / Flat 69) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000245 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $100.99

## 6. Latest Market Context

- 更新: 2026-07-20T09:21:02.248562+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=64096.1
- Funnel: target 884 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +104.42% | $14,498,229.57 |
| BANK/USDT:USDT | +57.86% | $111,034,016.61 |
| EVAA/USDT:USDT | +33.86% | $5,719,057.46 |
| PROM/USDT:USDT | +22.11% | $3,152,600.27 |
| PUMPFUN/USDT:USDT | +18.91% | $26,491,351.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.45% | +3.35% |
| SYN/USDT:USDT | below_1h_threshold | +3.39% | +3.28% |
| USELESS/USDT:USDT | below_1h_threshold | +2.75% | +2.65% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.27% | +2.16% |
| TRADOOR/USDT:USDT | below_1h_threshold | +1.84% | +1.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
