# Decision Report

- generated_at: 2026-10-23T16:26:43.270319+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17249**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17249, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-3.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.40% | **-3.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 10/20 | 50.0% | +5.60% | **+2.80%** |
| LIMIT_7PCT | 13/20 | 65.0% | +3.91% | **+2.54%** |
| LIMIT_9PCT | 9/20 | 45.0% | +5.33% | **+2.40%** |
| LIMIT_10PCT | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_6PCT | 15/20 | 75.0% | +1.98% | **+1.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +4.12% | **+4.12%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +6.91% | **+3.80%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +4.25% | **+3.61%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +5.93% | **+3.56%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +5.82% | **+3.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7257件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.29** / 初期 $100.00 (+198.29%)
- 確定: 3913件 (Win 1077 / Loss 910 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2598 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $298.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5411件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000610 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T16:26:22.571362+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=81467.2
- Funnel: target 1088 → liquid 171 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.3 >= 65=1, 4h RSI 78.0 >= 65=1, 4h RSI n/a=1, 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +22.43% | $40,560,259.79 |
| JCT/USDT:USDT | +13.52% | $5,473,118.81 |
| KIMCHI/USDT:USDT | +10.86% | $1,818,840.12 |
| BIRB/USDT:USDT | +6.11% | $2,956,559.46 |
| SOXS/USDT:USDT | +1.73% | $37,388,380.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.35% | +1.57% |
| AKE/USDT:USDT | below_1h_threshold | +1.20% | +1.43% |
| BMT/USDT:USDT | below_1h_threshold | +1.11% | +1.34% |
| ARK/USDT:USDT | below_1h_threshold | +1.01% | +1.23% |
| STRK/USDT:USDT | below_1h_threshold | +0.82% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
