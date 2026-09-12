# Decision Report

- generated_at: 2026-09-12T18:56:26.655515+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14320**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14320, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.10% | **+0.95%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.54% | **+0.75%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.50% | **+0.42%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.43% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.33% | **+1.87%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.80% | **+1.71%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.65% | **+1.07%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.51% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5452件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$212.73** / 初期 $100.00 (+112.73%)
- 確定: 2838件 (Win 782 / Loss 656 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $212.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.18** / 初期 $100.00 (+24.18%)
- 確定: 2771件 (Win 820 / Loss 1064 / Flat 887) / pending 5件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000455 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $124.18

## 6. Latest Market Context

- 更新: 2026-09-12T18:56:15.392112+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=77116.3
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.2 >= 65=1, 4h RSI 69.5 >= 65=1, 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIVER/USDT:USDT | +20.56% | $12,137,374.03 |
| STORJ/USDT:USDT | +20.35% | $28,561,738.74 |
| LONGXIA/USDT:USDT | +16.91% | $9,058,604.95 |
| REZ/USDT:USDT | +12.61% | $1,382,324.01 |
| FLOCK/USDT:USDT | +9.74% | $1,061,140.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +2.05% | +2.12% |
| INJ/USDT:USDT | below_1h_threshold | +0.69% | +0.77% |
| AKE/USDT:USDT | below_1h_threshold | +0.69% | +0.77% |
| VTHO/USDT:USDT | below_1h_threshold | +0.35% | +0.43% |
| CYS/USDT:USDT | below_1h_threshold | +0.28% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
