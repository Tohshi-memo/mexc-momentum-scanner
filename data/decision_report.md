# Decision Report

- generated_at: 2026-10-01T19:31:41.828334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15937**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15937, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.36% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.53% | **+1.90%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.13% | **+1.38%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.29% | **+1.09%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.52% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.60** / 初期 $100.00 (+1210.60%)
- 確定: 6046件 (Win 1793 / Loss 1950 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,310.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$279.91** / 初期 $100.00 (+179.91%)
- 確定: 3590件 (Win 1002 / Loss 834 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1086 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $279.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4103件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T19:31:26.113109+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=84600.0
- Funnel: target 1097 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +117.88% | $1,441,783.26 |
| MAGMA/USDT:USDT | +19.41% | $1,064,351.55 |
| LONGXIA/USDT:USDT | +12.27% | $11,012,351.56 |
| MUU/USDT:USDT | +7.83% | $20,632,367.71 |
| ZRO/USDT:USDT | +6.48% | $6,086,942.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALICE/USDT:USDT | below_1h_threshold | +4.33% | +4.52% |
| MAGMA/USDT:USDT | below_1h_threshold | +3.81% | +4.01% |
| KORU/USDT:USDT | below_1h_threshold | +1.25% | +1.45% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.95% | +1.14% |
| GRASS/USDT:USDT | below_1h_threshold | +0.93% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
