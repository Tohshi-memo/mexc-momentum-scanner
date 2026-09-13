# Decision Report

- generated_at: 2026-09-13T03:41:36.634008+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14368**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14368, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 11/20 | 55.0% | +0.34% | **+0.19%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_8PCT | 9/20 | 45.0% | -0.48% | **-0.21%** |
| LIMIT_5PCT | 13/20 | 65.0% | -0.63% | **-0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/10 | 50.0% | +5.02% | **+2.51%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.02% | **+1.92%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.87% | **+1.72%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.01% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5499件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$221.01** / 初期 $100.00 (+121.01%)
- 確定: 2886件 (Win 800 / Loss 676 / Flat 1410) / skip 4893件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $221.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.02** / 初期 $100.00 (+27.02%)
- 確定: 2818件 (Win 839 / Loss 1084 / Flat 895) / pending 6件 / skip 3017件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000426 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $127.02

## 6. Latest Market Context

- 更新: 2026-09-13T03:41:20.868067+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=77179.5
- Funnel: target 1068 → liquid 127 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 99.3 >= 65=1, 4h RSI 70.3 >= 65=1, 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +590.49% | $77,440,324.98 |
| POWR/USDT:USDT | +47.66% | $1,701,795.83 |
| ZCAT/USDT:USDT | +45.96% | $1,186,135.16 |
| LONGXIA/USDT:USDT | +18.91% | $9,880,143.78 |
| STORJ/USDT:USDT | +18.89% | $19,057,946.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +3.82% | +3.93% |
| FLOCK/USDT:USDT | below_1h_threshold | +3.03% | +3.14% |
| POWR/USDT:USDT | below_1h_threshold | +1.87% | +1.98% |
| BSV/USDT:USDT | below_1h_threshold | +1.37% | +1.48% |
| ILV/USDT:USDT | below_1h_threshold | +1.10% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
