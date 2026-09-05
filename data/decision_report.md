# Decision Report

- generated_at: 2026-09-05T17:36:34.019336+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13762**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13762, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.77% | **+0.31%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.20% | **-0.15%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.32% | **+0.73%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.97% | **+0.69%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.80% | **+0.60%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.76% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.61** / 初期 $100.00 (+755.61%)
- 確定: 5068件 (Win 1521 / Loss 1653 / Flat 1894) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $855.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.86** / 初期 $100.00 (+87.86%)
- 確定: 2507件 (Win 698 / Loss 591 / Flat 1218) / skip 4666件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0288 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $187.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.32** / 初期 $100.00 (+19.32%)
- 確定: 2382件 (Win 706 / Loss 904 / Flat 772) / pending 4件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.32

## 6. Latest Market Context

- 更新: 2026-09-05T17:36:18.995403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80006.5
- Funnel: target 1050 → liquid 129 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1, 4h RSI 73.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +18.73% | $2,494,363.53 |
| 4/USDT:USDT | +16.19% | $24,613,419.29 |
| MAGMA/USDT:USDT | +13.79% | $2,178,963.00 |
| USELESS/USDT:USDT | +13.51% | $20,505,344.32 |
| MARSCOIN/USDT:USDT | +9.18% | $8,937,198.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.70% | +4.69% |
| AKE/USDT:USDT | below_1h_threshold | +4.59% | +4.58% |
| BASECAT/USDT:USDT | below_1h_threshold | +2.74% | +2.73% |
| USELESS/USDT:USDT | below_1h_threshold | +2.59% | +2.59% |
| B/USDT:USDT | below_1h_threshold | +2.03% | +2.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
