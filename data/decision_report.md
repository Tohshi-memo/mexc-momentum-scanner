# Decision Report

- generated_at: 2026-10-24T00:26:34.582671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17304**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17304, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 11/20 | 55.0% | +4.69% | **+2.58%** |
| LIMIT_7PCT | 9/20 | 45.0% | +4.93% | **+2.22%** |
| LIMIT_8PCT | 7/20 | 35.0% | +5.67% | **+1.99%** |
| LIMIT_9PCT | 5/20 | 25.0% | +4.92% | **+1.23%** |
| LIMIT_5PCT | 13/20 | 65.0% | +1.60% | **+1.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.16% | **+0.69%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,317.21** / 初期 $100.00 (+1217.21%)
- 確定: 6558件 (Win 1903 / Loss 2095 / Flat 2560) / skip 7307件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BIRB/USDT:USDT `LIMIT_9PCT` EXPIRED account +0.00% 残高後 $1,317.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3929件 (Win 1083 / Loss 920 / Flat 1926) / skip 6786件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1088 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5465件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000299 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T00:26:14.232550+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.47% price=80778.5
- Funnel: target 1088 → liquid 167 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1, 4h RSI 69.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +38.94% | $4,257,812.37 |
| IRYS/USDT:USDT | +30.21% | $96,014,718.49 |
| AXIS/USDT:USDT | +26.80% | $1,615,159.72 |
| AGT/USDT:USDT | +26.44% | $10,791,403.12 |
| SOXS/USDT:USDT | +4.33% | $31,752,021.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXIS/USDT:USDT | below_1h_threshold | +2.62% | +3.09% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +1.35% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.74% | +1.21% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +1.18% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.56% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
