# Decision Report

- generated_at: 2026-07-25T16:21:20.861652+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9529**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9529, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.69% | **-1.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/17 | 29.4% | +2.64% | **+0.78%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.33% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.68% | **+2.94%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.83% | **+2.41%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.88% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$447.40** / 初期 $100.00 (+347.40%)
- 確定: 3357件 (Win 1063 / Loss 1087 / Flat 1207) / skip 2733件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $447.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$135.91** / 初期 $100.00 (+35.91%)
- 確定: 1182件 (Win 323 / Loss 257 / Flat 602) / skip 1758件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1849 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $135.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.96** / 初期 $100.00 (+7.96%)
- 確定: 575件 (Win 195 / Loss 220 / Flat 160) / pending 6件 / skip 422件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000588 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $107.96

## 6. Latest Market Context

- 更新: 2026-07-25T16:21:11.887678+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64137.2
- Funnel: target 898 → liquid 138 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +13.71% | $133,436,758.92 |
| BANK/USDT:USDT | +12.16% | $86,750,727.28 |
| SHIB/USDT:USDT | +2.94% | $8,573,889.49 |
| FLOKI/USDT:USDT | +2.90% | $1,125,507.90 |
| RIF/USDT:USDT | +1.91% | $3,720,029.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOKI/USDT:USDT | below_1h_threshold | +2.90% | +2.92% |
| SHIB/USDT:USDT | below_1h_threshold | +2.13% | +2.15% |
| RIF/USDT:USDT | below_1h_threshold | +1.91% | +1.93% |
| US/USDT:USDT | below_1h_threshold | +1.68% | +1.70% |
| ALLO/USDT:USDT | below_1h_threshold | +1.68% | +1.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
