# Decision Report

- generated_at: 2026-10-01T14:41:54.674639+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15909**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15909, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.34% | **-1.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +3.27% | **+0.49%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.32% | **+0.11%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.57% | **+1.41%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.82% | **+1.18%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.52% | **+1.09%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.97% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,314.06** / 初期 $100.00 (+1214.06%)
- 確定: 6024件 (Win 1785 / Loss 1937 / Flat 2302) / skip 6446件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,314.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.68** / 初期 $100.00 (+176.68%)
- 確定: 3562件 (Win 990 / Loss 819 / Flat 1753) / skip 5758件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1411 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $276.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4072件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000365 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T14:41:33.487308+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=84046.9
- Funnel: target 1097 → liquid 175 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +78.07% | $7,232,995.95 |
| MOVR/USDT:USDT | +51.74% | $21,072,509.61 |
| CAP/USDT:USDT | +27.45% | $1,074,239.39 |
| CT/USDT:USDT | +21.41% | $7,207,861.79 |
| ACNSTOCK/USDT:USDT | +21.28% | $2,309,239.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_relative_strength | +5.15% | +4.99% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +3.79% | +3.62% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.05% |
| STX/USDT:USDT | below_1h_threshold | +1.57% | +1.41% |
| TWSTSTOCK/USDT:USDT | below_1h_threshold | +1.47% | +1.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
