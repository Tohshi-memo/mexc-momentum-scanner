# Decision Report

- generated_at: 2026-08-26T13:31:28.350830+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12711**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.24% / filled 20/20。**
- 全期間 MARKET基準: n=12711, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.77% | **+1.59%** |
| LIMIT_BB3S | 10/16 | 62.5% | +1.79% | **+1.12%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.79% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.24% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.24% | **-0.12%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.43% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$690.03** / 初期 $100.00 (+590.03%)
- 確定: 4610件 (Win 1400 / Loss 1516 / Flat 1694) / skip 4662件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $690.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4121件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0757 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.00** / 初期 $100.00 (+16.00%)
- 確定: 1980件 (Win 580 / Loss 756 / Flat 644) / pending 2件 / skip 2200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.00

## 6. Latest Market Context

- 更新: 2026-08-26T13:31:16.543726+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=78124.8
- Funnel: target 1023 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +272.37% | $19,748,490.28 |
| TAC/USDT:USDT | +51.06% | $8,147,528.17 |
| BMT/USDT:USDT | +49.28% | $16,246,706.14 |
| LONGXIA/USDT:USDT | +36.45% | $2,002,280.19 |
| ONG/USDT:USDT | +20.18% | $10,029,291.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| METASTOCK/USDT:USDT | below_1h_threshold | +2.27% | +2.47% |
| TAC/USDT:USDT | below_1h_threshold | +2.14% | +2.34% |
| EDEN/USDT:USDT | below_1h_threshold | +2.02% | +2.22% |
| SOXS/USDT:USDT | below_1h_threshold | +1.91% | +2.10% |
| ONT/USDT:USDT | below_1h_threshold | +1.87% | +2.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
