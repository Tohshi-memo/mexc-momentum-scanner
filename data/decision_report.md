# Decision Report

- generated_at: 2026-09-05T17:26:34.318650+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13761**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13761, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.77% | **+0.31%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_ATR | 16/20 | 80.0% | -0.20% | **-0.16%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.85% | **+0.93%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.91** / 初期 $100.00 (+759.91%)
- 確定: 5067件 (Win 1521 / Loss 1652 / Flat 1894) / skip 5255件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $859.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.52** / 初期 $100.00 (+88.52%)
- 確定: 2506件 (Win 698 / Loss 590 / Flat 1218) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0264 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $188.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.53** / 初期 $100.00 (+19.53%)
- 確定: 2381件 (Win 706 / Loss 903 / Flat 772) / pending 5件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000231 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $119.53

## 6. Latest Market Context

- 更新: 2026-09-05T17:26:18.753157+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80039.9
- Funnel: target 1050 → liquid 128 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 72.9 >= 65=1, 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +20.81% | $2,378,725.55 |
| 4/USDT:USDT | +14.35% | $24,497,621.66 |
| USELESS/USDT:USDT | +14.03% | $20,337,402.88 |
| MAGMA/USDT:USDT | +13.77% | $2,151,784.77 |
| MARSCOIN/USDT:USDT | +9.54% | $8,870,863.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.09% | +3.04% |
| AKE/USDT:USDT | below_1h_threshold | +2.87% | +2.82% |
| BASECAT/USDT:USDT | below_1h_threshold | +2.37% | +2.32% |
| LINK/USDT:USDT | below_1h_threshold | +2.22% | +2.18% |
| PONS/USDT:USDT | below_1h_threshold | +1.74% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
