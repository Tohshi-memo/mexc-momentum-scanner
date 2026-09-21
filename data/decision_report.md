# Decision Report

- generated_at: 2026-09-21T17:26:32.659817+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15274**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15274, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +1.31% | **+1.05%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.88% | **+0.22%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.27% | **+0.08%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.16% | **-0.06%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 15/20 | 75.0% | +3.18% | **+2.39%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.22% | **+2.09%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.47% | **+1.85%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.22% | **+1.61%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.64% | **+1.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.65** / 初期 $100.00 (+1095.65%)
- 確定: 5765件 (Win 1716 / Loss 1851 / Flat 2198) / skip 6070件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $1,195.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.64** / 初期 $100.00 (+146.64%)
- 確定: 3317件 (Win 915 / Loss 766 / Flat 1636) / skip 5368件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0410 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CHIP/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $246.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.68** / 初期 $100.00 (+22.68%)
- 確定: 3047件 (Win 895 / Loss 1191 / Flat 961) / pending 5件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CHIP/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $122.68

## 6. Latest Market Context

- 更新: 2026-09-21T17:26:23.144212+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=85822.0
- Funnel: target 1055 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FORM/USDT:USDT | +32.20% | $4,459,144.69 |
| SYN/USDT:USDT | +9.92% | $4,110,480.72 |
| ALLO/USDT:USDT | +8.01% | $1,941,672.98 |
| BTW/USDT:USDT | +3.06% | $4,439,728.28 |
| USELESS/USDT:USDT | +2.90% | $4,821,272.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.96% | +2.07% |
| METASTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.22% |
| DOGE/USDT:USDT | below_1h_threshold | +1.02% | +1.13% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.99% | +1.10% |
| KORU/USDT:USDT | below_1h_threshold | +0.90% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
