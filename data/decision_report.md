# Decision Report

- generated_at: 2026-09-16T03:51:50.250055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14629**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.46% / filled 20/20。**
- 全期間 MARKET基準: n=14629, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.46% | **+3.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.46% | **+3.46%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.41% | **+2.73%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.93% | **+1.91%** |
| LIMIT_ATR | 11/20 | 55.0% | +3.33% | **+1.83%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.59% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_7PCT_LONG | 13/20 | 65.0% | +0.07% | **+0.05%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -1.19% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,044.12** / 初期 $100.00 (+944.12%)
- 確定: 5517件 (Win 1645 / Loss 1786 / Flat 2086) / skip 5673件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,044.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3054件 (Win 839 / Loss 719 / Flat 1496) / skip 4986件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0238 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.58** / 初期 $100.00 (+25.58%)
- 確定: 2920件 (Win 869 / Loss 1138 / Flat 913) / pending 4件 / skip 3177件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $125.58

## 6. Latest Market Context

- 更新: 2026-09-16T03:51:30.013894+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=75742.5
- Funnel: target 1064 → liquid 154 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +28.06% | $2,199,782.28 |
| ON/USDT:USDT | +15.58% | $3,122,962.37 |
| LSK/USDT:USDT | +14.85% | $16,702,693.06 |
| LONGXIA/USDT:USDT | +14.42% | $1,853,074.82 |
| USELESS/USDT:USDT | +9.17% | $5,094,762.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +3.98% | +4.12% |
| KORU/USDT:USDT | below_1h_threshold | +2.71% | +2.85% |
| BTW/USDT:USDT | below_1h_threshold | +2.19% | +2.34% |
| ON/USDT:USDT | below_1h_threshold | +1.74% | +1.88% |
| SNXX/USDT:USDT | below_1h_threshold | +1.68% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
