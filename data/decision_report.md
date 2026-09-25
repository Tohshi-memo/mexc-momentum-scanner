# Decision Report

- generated_at: 2026-09-25T23:26:28.010797+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15548**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15548, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.12% | **-1.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.42% | **+0.27%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.04% | **+0.03%** |
| LIMIT_BB3S | 4/15 | 26.7% | -0.31% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.75% | **+1.10%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.01%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.95% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$120.55** / 初期 $100.00 (+20.55%)
- 確定トレード: 222件 (TP 81 / SL 135 / EXP 6)
- 最新: APT/USDT:USDT EXPIRED PnL -0.12% 残高後 $120.55
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,192.51** / 初期 $100.00 (+1092.51%)
- 確定: 5912件 (Win 1743 / Loss 1896 / Flat 2273) / skip 6197件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,192.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.68** / 初期 $100.00 (+156.68%)
- 確定: 3481件 (Win 954 / Loss 793 / Flat 1734) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0439 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $256.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.38** / 初期 $100.00 (+19.38%)
- 確定: 3178件 (Win 934 / Loss 1259 / Flat 985) / pending 4件 / skip 3839件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.38

## 6. Latest Market Context

- 更新: 2026-09-25T23:26:14.772517+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=83978.1
- Funnel: target 1067 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +20.94% | $1,121,238.65 |
| BR/USDT:USDT | +15.29% | $9,254,857.08 |
| PHA/USDT:USDT | +15.19% | $24,012,545.19 |
| SEI/USDT:USDT | +11.71% | $33,803,413.92 |
| ARK/USDT:USDT | +11.34% | $2,855,803.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +2.99% | +3.06% |
| ONE/USDT:USDT | below_1h_threshold | +2.53% | +2.60% |
| OP/USDT:USDT | below_1h_threshold | +2.45% | +2.51% |
| SUI/USDT:USDT | below_1h_threshold | +1.97% | +2.03% |
| CHIP/USDT:USDT | below_1h_threshold | +1.94% | +2.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
