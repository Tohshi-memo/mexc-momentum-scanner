# Decision Report

- generated_at: 2026-11-08T17:11:20.529605+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18470**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18470, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.11% | **+0.74%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.54% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +4.52% | **+2.93%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.36% | **+2.62%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.91% | **+2.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.65% | **+1.73%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +5.39% | **+1.62%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,667.41** / 初期 $100.00 (+1567.41%)
- 確定: 7151件 (Win 2057 / Loss 2280 / Flat 2814) / skip 7880件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIOT/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,667.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7126件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1836 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6630件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000537 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T17:11:07.398070+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=75725.0
- Funnel: target 1089 → liquid 103 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIOT/USDT:USDT | +13.44% | $4,313,841.15 |
| JCT/USDT:USDT | +12.66% | $30,051,527.20 |
| SKYAI/USDT:USDT | +2.26% | $1,211,495.52 |
| Q/USDT:USDT | +0.91% | $2,336,436.68 |
| KOMA/USDT:USDT | +0.76% | $1,210,006.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +1.01% | +1.03% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.97% | +0.99% |
| AGT/USDT:USDT | below_1h_threshold | +0.86% | +0.88% |
| MET/USDT:USDT | below_1h_threshold | +0.56% | +0.58% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.28% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
