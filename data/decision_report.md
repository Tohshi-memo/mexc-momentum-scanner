# Decision Report

- generated_at: 2026-08-13T10:16:20.988918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11435**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=11435, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.54% | **+1.46%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.39% | **+1.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.22% | **+0.91%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.44% | **+0.86%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.02% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 16/20 | 80.0% | +1.78% | **+1.42%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.43% | **+1.36%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.42% | **+1.20%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.54** / 初期 $100.00 (+514.54%)
- 確定: 3953件 (Win 1235 / Loss 1292 / Flat 1426) / skip 4043件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLUAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $614.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.68** / 初期 $100.00 (+49.68%)
- 確定: 1623件 (Win 462 / Loss 385 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1321 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $149.68

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.19** / 初期 $100.00 (+16.19%)
- 確定: 1442件 (Win 424 / Loss 542 / Flat 476) / pending 3件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLUAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.19

## 6. Latest Market Context

- 更新: 2026-08-13T10:16:11.312466+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=63607.5
- Funnel: target 973 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVAAI/USDT:USDT | +32.36% | $1,064,775.53 |
| ACU/USDT:USDT | +18.82% | $6,420,780.53 |
| BTW/USDT:USDT | +18.61% | $26,045,013.24 |
| AKE/USDT:USDT | +16.21% | $2,710,099.67 |
| BANK/USDT:USDT | +14.60% | $4,946,263.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVAAI/USDT:USDT | below_1h_threshold | +3.85% | +4.08% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +2.84% | +3.08% |
| COTI/USDT:USDT | below_1h_threshold | +2.56% | +2.79% |
| VELVET/USDT:USDT | below_1h_threshold | +1.47% | +1.70% |
| BR/USDT:USDT | below_1h_threshold | +1.26% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
