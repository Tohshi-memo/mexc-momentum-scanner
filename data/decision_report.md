# Decision Report

- generated_at: 2026-06-03T11:08:47.959461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5541**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5541, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.44% | **+0.37%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.34% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.61% | **+0.49%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.02% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$134.35** / 初期 $100.00 (+34.35%)
- 確定: 995件 (Win 238 / Loss 306 / Flat 451) / skip 1107件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $134.35

## 4. Latest Market Context

- 更新: 2026-06-03T11:08:45.954598+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=67193.9
- Funnel: target 771 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +47.90% | $3,073,992.56 |
| CLO/USDT:USDT | +42.00% | $4,423,902.41 |
| WLD/USDT:USDT | +28.13% | $161,468,680.40 |
| ENA/USDT:USDT | +27.35% | $57,290,320.38 |
| PORTAL/USDT:USDT | +27.32% | $14,687,566.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +4.26% | +4.36% |
| PORTAL/USDT:USDT | below_1h_threshold | +3.02% | +3.12% |
| ETHFI/USDT:USDT | below_1h_threshold | +2.38% | +2.48% |
| GENIUS/USDT:USDT | below_1h_threshold | +2.21% | +2.31% |
| WLD/USDT:USDT | below_1h_threshold | +1.73% | +1.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
