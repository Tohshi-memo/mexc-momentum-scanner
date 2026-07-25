# Decision Report

- generated_at: 2026-07-25T15:06:19.397726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9523**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9523, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/20 | 30.0% | +2.32% | **+0.70%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.57% | **+1.93%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.20% | **+1.87%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$446.26** / 初期 $100.00 (+346.26%)
- 確定: 3351件 (Win 1061 / Loss 1085 / Flat 1205) / skip 2733件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $446.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$135.23** / 初期 $100.00 (+35.23%)
- 確定: 1177件 (Win 321 / Loss 256 / Flat 600) / skip 1757件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1702 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $135.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.88** / 初期 $100.00 (+7.88%)
- 確定: 570件 (Win 194 / Loss 218 / Flat 158) / pending 4件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000610 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $107.88

## 6. Latest Market Context

- 更新: 2026-07-25T15:06:11.114166+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64159.4
- Funnel: target 898 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +74.09% | $126,283,070.74 |
| EUL/USDT:USDT | +48.63% | $12,028,252.33 |
| AKE/USDT:USDT | +27.21% | $47,176,998.92 |
| SYN/USDT:USDT | +17.23% | $2,682,363.24 |
| BANK/USDT:USDT | +16.51% | $76,536,780.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.70% | +3.73% |
| SLX/USDT:USDT | below_1h_threshold | +1.11% | +1.14% |
| SHIB/USDT:USDT | below_1h_threshold | +0.85% | +0.89% |
| DOGE/USDT:USDT | below_1h_threshold | +0.53% | +0.56% |
| TRB/USDT:USDT | below_1h_threshold | +0.41% | +0.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
