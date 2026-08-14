# Decision Report

- generated_at: 2026-08-14T20:51:36.304337+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11605**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11605, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.78% | **+0.70%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.21% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.42% | **+1.88%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +4.34% | **+1.52%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.41% | **+1.20%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.65% | **+1.19%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.32% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$638.55** / 初期 $100.00 (+538.55%)
- 確定: 4073件 (Win 1277 / Loss 1341 / Flat 1455) / skip 4093件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WLFI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $638.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$151.92** / 初期 $100.00 (+51.92%)
- 確定: 1670件 (Win 478 / Loss 404 / Flat 788) / skip 3346件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0551 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: WLFI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $151.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.41** / 初期 $100.00 (+17.41%)
- 確定: 1553件 (Win 472 / Loss 595 / Flat 486) / pending 5件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000218 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.41

## 6. Latest Market Context

- 更新: 2026-08-14T20:51:22.136365+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=62907.4
- Funnel: target 985 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +22.77% | $6,747,765.34 |
| DOLO/USDT:USDT | +22.77% | $1,469,347.30 |
| ACE/USDT:USDT | +13.53% | $62,005,913.29 |
| CYS/USDT:USDT | +10.54% | $14,098,834.39 |
| VELVET/USDT:USDT | +9.69% | $41,777,038.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.88% | +2.93% |
| VELVET/USDT:USDT | below_1h_threshold | +2.78% | +2.84% |
| SOXL/USDT:USDT | below_1h_threshold | +2.73% | +2.78% |
| ACU/USDT:USDT | below_1h_threshold | +2.00% | +2.05% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.96% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
