# Decision Report

- generated_at: 2026-10-23T16:46:38.744924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17257**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17257, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 8/20 | 40.0% | +5.00% | **+2.00%** |
| LIMIT_9PCT | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_7PCT | 8/20 | 40.0% | +2.85% | **+1.14%** |
| LIMIT_10PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.08% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +3.22% | **+3.22%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.15% | **+2.52%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.87% | **+2.32%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.64% | **+2.00%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +5.54% | **+1.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.72** / 初期 $100.00 (+1210.72%)
- 確定: 6553件 (Win 1902 / Loss 2094 / Flat 2557) / skip 7265件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNITREE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,310.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$300.75** / 初期 $100.00 (+200.75%)
- 確定: 3921件 (Win 1081 / Loss 914 / Flat 1926) / skip 6747件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2451 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $300.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5417件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000604 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T16:46:21.211534+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=81759.9
- Funnel: target 1088 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.7 >= 65=1, 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +52.10% | $46,224,098.92 |
| KIMCHI/USDT:USDT | +6.69% | $1,832,527.35 |
| BMT/USDT:USDT | +1.92% | $1,045,936.89 |
| MSTRSTOCK/USDT:USDT | +1.85% | $15,380,703.22 |
| SOXS/USDT:USDT | +1.33% | $37,718,215.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +1.92% | +1.79% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.35% | +1.21% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.27% | +1.14% |
| CHIP/USDT:USDT | below_1h_threshold | +1.24% | +1.11% |
| ENA/USDT:USDT | below_1h_threshold | +1.21% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
