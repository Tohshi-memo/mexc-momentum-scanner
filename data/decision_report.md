# Decision Report

- generated_at: 2026-06-13T17:53:31.100161+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6594**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6594, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.62% | **-1.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.08% | **+0.07%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.63% | **+1.45%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.68% | **+1.34%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.81% | **+1.18%** |
| ASK_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.03% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.73** / 初期 $100.00 (+66.73%)
- 確定: 1467件 (Win 393 / Loss 465 / Flat 609) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $166.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.15** / 初期 $100.00 (+0.15%)
- 確定: 6件 (Win 2 / Loss 1 / Flat 3) / skip 0件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0320 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $100.15

## 5. Latest Market Context

- 更新: 2026-06-13T17:53:26.849114+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63952.1
- Funnel: target 770 → liquid 141 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +12.01% | $66,949,907.81 |
| COAI/USDT:USDT | +6.70% | $23,109,927.53 |
| NOT/USDT:USDT | +4.14% | $2,676,907.01 |
| SKYAI/USDT:USDT | +3.13% | $18,760,597.28 |
| TAO/USDT:USDT | +3.01% | $245,077,252.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +4.61% | +4.68% |
| FET/USDT:USDT | below_1h_threshold | +2.64% | +2.71% |
| TAO/USDT:USDT | below_1h_threshold | +2.27% | +2.34% |
| AIO/USDT:USDT | below_1h_threshold | +2.15% | +2.22% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.96% | +2.03% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
